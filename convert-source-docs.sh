# !/bin/bash
for filename in init_docs/source/*; 
    do filen="${filename##*/}";
    new_file_path="./init_docs/text/${filen%.*}.txt";

    generated=true
    case "${filen}" in
        *.pdf) pdftotext -raw "${filename}" "${new_file_path}" ;;
        *.docx) textutil -convert txt "${filename}"; mv "./init_docs/source/${filen%.*}.txt" "${new_file_path}";;
        *) generated=false; echo "File extension not supported for text extraction/conversion" ;;
    esac
    if [ "$generated" = true ] ; then
        echo "Generated ${new_file_path}"
    fi
done