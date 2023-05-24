const fs = require('fs');

const dictionaryFile = process.argv[2] || './preferred-stock.json';

const readDictionary = () => new Promise((resolve, reject) => {
    fs.readFile(dictionaryFile, (err, data) => {
        if (err) {
            reject(err)
        }
        resolve(JSON.parse(data))
    });
});

const readTextFile = fileName => new Promise((resolve, reject) => {
    fs.readFile(fileName, (err, data) => {
        if (err) {
            reject(err);
        }
        resolve(data);
    })
});

const readTextFiles = () => new Promise((resolve, reject) => {
    fs.readdir('./init_docs/text', async (err, data) => {
        try {
            if (err) {
                throw err;
            }
            const textContent = await Promise.all(data.map(async f => {
                const path = `./init_docs/text/${f}`;
                return (await readTextFile(path)).toString();
            }));
            resolve(textContent.join('\n'));
        } catch(error) {
            reject(error);
        }
    });
});

function getIndicesOf(searchStr, str, caseSensitive = false) {
    var searchStrLen = searchStr.length;
    if (searchStrLen == 0) {
        return [];
    }
    var startIndex = 0, index, indices = [];
    if (!caseSensitive) {
        str = str.toLowerCase();
        searchStr = searchStr.toLowerCase();
    }
    while ((index = str.indexOf(searchStr, startIndex)) > -1) {
        indices.push(index);
        startIndex = index + searchStrLen;
    }
    return indices;
}

(async function() {
    try {
        const { entities } = await readDictionary();
        const rawText = await readTextFiles();
        const rawTextSplit = rawText.split("\n");
        for (const entity of entities) {
            const { id, normalizedText } = entity;
            const label = id.replace(/[-]/g, "_");
            const ents = [];
            for (const nText of normalizedText) {
                let matches = rawTextSplit.map(text => {
                    let textToCheck = nText.split("...");
                    const containsGap = textToCheck.length > 1;
                    
                    const target = containsGap 
                        ? textToCheck.filter(t => t.indexOf("[") > -1)[0].replace(/[^A-Z\s/]/gi, '') : textToCheck[0];
                    if (containsGap) {
                        textToCheck = textToCheck.map(t => t.replace(/[^A-Z\s/]/gi, ''));
                    }
                    const remaining = textToCheck.filter(nt => text.toLowerCase().indexOf(nt.toLowerCase()) > -1);
                    if (textToCheck.length === remaining.length) {
                        if (containsGap) {
                            const fidxs = getIndicesOf(textToCheck[0], text)
                            const lidxs = getIndicesOf(textToCheck[1], text).map(i => i + textToCheck[1].length)
                            const idxs = fidxs.map((fi, i) => lidxs[i] && fi < lidxs[i] ? [fi, lidxs[i]] : null).filter(i => !!i);
                            let found = idxs.map(idxSet => {
                                return text.substring(...idxSet)
                            });
                            found = found.map((t, i) => {
                                const tidx = t.toLowerCase().indexOf(target.toLowerCase());
                                const idxs = [tidx, tidx + target.length]
                                return {
                                    t,
                                    idxs: [idxs]
                                }
                            });
                            
                            if (found.length) {
                                return { found };
                            }
                        } else {
                            const idxs = getIndicesOf(textToCheck[0], text).map(i => [i, i + target.length]);
                            return { t: text, idxs };
                        }
                    }
                    return null;
                });
                const _matches = matches.slice();
                _matches.forEach((m, i) => {
                    if (m && Object.keys(m).indexOf('found') > -1) {
                        matches.push(...m.found);
                        matches[i] = null;
                    }
                });
                matches = matches.filter(m => !!m);
                // console.log(matches);
                if (matches.length) {
                    ents.push(...matches);
                }
            }
            if (ents.length) {
                const filename = `./training-data/${label}.json`;
                fs.writeFile(filename, JSON.stringify({
                    entities: ents
                }, null, 2), (err) => {
                    if (err) {
                        throw err;
                    }
                    console.log(`Generated ${filename}`);
                });
            }
        }
    } catch(err) {
        console.log(err)
    }
})()


