import json
output = [
    ('pricing\n         between the shares of ', '9dcb939e-e467-490a-97a5-1c7c2f32b31d',
     'SERIES_PREF', 'Series B Preferred Stock', 'issued and sold prior to '),
    ('of this\n         Agreement, at ', 'db124ba2-eaf1-473d-9d76-0046e59a4dc9',
     'ORG', 'the Closing the Company', 'shall issue an amount of '),
    ('an amount of additional shares of ', '3e899d92-935d-45e7-a91d-9462c3dbf4b5', 'SERIES_PREF',
     'Series B\n         Preferred Stock', 'to each stockholder holding Series B Preferred '),
    ('of Series B\n         Preferred Stock to each stockholder holding ',
     'c3a1df59-bf4d-4e8a-9730-0e6ecfea6f1a', 'SERIES_PREF', 'Series B Preferred', 'Shares prior to the Closing '),
    (', the number of shares of ', 'aaf06667-1ab4-4ff3-a70a-2597d3a56e50',
     'SERIES_PREF', 'Series B\n         Preferred Stock', 'held by such stockholder, '),
    ('), the number of shares of ', 'dfdcabf5-367a-4b16-986d-761567f852ef',
     'SERIES_PREF', 'Series B Preferred\n         Stock', 'which would have been held '),
    ('together with the total number of ', '44ab62be-d3e0-41c3-ba26-58a6ef967a9b',
     'SERIES_PREF', 'Series B Preferred', 'Shares held by such shareholder'),
    ('shall be converted into Shares of ', '2300d5f0-1372-49f1-88c3-d32d9cf0889e',
     'SERIES_PREF', 'Series B Preferred Stock', '. The number of shares '),
    ('\n\x0cCerahelix, Inc. - 2018 ', '818f0a83-4de8-498e-91a2-b64b6ab8d6db', 'SERIES_PREF',
     'Series B                                                                        Page 3 of 126\nInvestment Binder - PropelX', '\n\n\n\n\n         together with accrued interest '),
    ('together with accrued interest by the ', '3ed638ef-8597-45d8-82f0-36ae78f9761e',
     'SERIES_PREF', 'Series B Purchase', 'Price. The principal balance '),
    ('Company shall issue a warrant to ', '9b07ae9e-7d7c-4551-bb1f-7c451b8a43e2',
     'ORG', 'PureTerra Ventures', '(or its designee) '),
    ('), to\n         purchase up to ', 'faab4cf9-8e23-4f18-a4cb-c00ce658d487',
     'CARDINAL', '1,824,054', 'additional shares of Series B Preferred Stock at '),
    ('up to 1,824,054 additional shares of ', 'bb02a0ba-ee27-4858-a931-9e8bacdab984',
     'SERIES_PREF', 'Series B Preferred Stock', 'at a price per share '),
    ('price per share of\n         $', 'ec72a16f-fd5b-41a9-8917-cd1c9badbbd7',
     'MONEY', '0.001', 'per share (the “'),
    ('using commercially\n         reasonable efforts, ', 'f8a52402-ac57-45de-aebc-679e61d4e4ab',
     'ORG', 'PureTerra Ventures', 'is unable to qualify as '),
    ('venture capital fund under the\n         ', '38c19c6c-1e8f-4c2a-9350-173334adccc3', 'ORG',
     'Maine Seed Capital Tax Credit Program', '.\n\n                         1.7    Defined '),
    ('as\n         of the date of ', '1c1de5d2-c8c0-434d-a663-25b43f69cf48',
     'ORG', 'the Initial Closing', ', in the form of '),
    ('dated as of the date of ', '2bc05869-1617-4f01-914e-fd2467efc2a8',
     'ORG', 'the Initial Closing', ', in the form of '),
    ('as of\n         the date of ', 'ead1c22c-0e23-4e32-aaa5-c12720406fc1',
     'ORG', 'the Initial Closing', ', in the form of '),
    ('means the Internal Revenue Code of ', 'a2c5bff8-c978-4eee-84ba-ebbcf8dc9836',
     'DATE', '1986', ', as amended.\n\n                                 '),
    ('purposes of Rule 506 promulgated under ', '8eb1ab14-41e4-493b-97f7-03ac63665d41',
     'LAW', 'the Securities Act', ', any Person listed\n         '),
    ('any Person listed\n         in the ', 'e0143321-374e-48e1-b4be-02ebb04d2816',
     'ORDINAL', 'first', 'paragraph of Rule 506(d)(1)'),
    ('EP - 02705706 - v3 }', 'bfee3a03-d635-4924-b542-1f56d1c6afef',
     'GPE', '', 'Cerahelix, Inc. - 2018 '),
    ('\n\x0cCerahelix, Inc. - 2018 ', 'aef62dae-ef5c-4c0c-a1f6-d29c864e90ad',
     'SERIES_PREF', 'Series B', 'Page 4 of 126\nInvestment Binder - '),
    ('Cerahelix, Inc. - 2018 Series B                                                                          ',
     '1838d7f5-c312-4bfd-a989-7e6db535b9bf', 'PERSON', 'Page 4', 'of 126\nInvestment Binder - PropelX'),
    ('- 2018 Series B                                                                          Page 4 of 126',
     'd9cf2555-2a1f-46d9-8650-a3251a0abcea', 'ORG', 'Investment Binder', '- PropelX\n\n\n\n\n                                (h'),
    ('    “Securities Act” means ', '19e97aa0-cb1a-4b94-9b0e-3508a6cfc21a',
     'LAW', 'the Securities Act', 'of 1933, as amended'),
    ('Securities Act” means the Securities Act of ',
     '0219fb22-058d-4c89-999e-177c6b9e42af', 'DATE', '1933', ', as amended,\n         '),
    ('Shares” means the shares of ', '813d9d68-a288-4d9f-a5e0-55e1395f52c0',
     'SERIES_PREF', 'Series B Preferred Stock', 'issued at\n         the Initial '),
    ('laws\n         of the State of ', '89046ecb-3bf2-41a6-b85b-d4dab038b5ba',
     'GPE', 'Delaware', 'and has all requisite corporate '),
    ('EP - 02705706 - v3 }', '7a16c509-0fad-487e-a5d1-3af56d43a479',
     'GPE', '', 'Cerahelix, Inc. - 2018 '),
    ('\n\x0cCerahelix, Inc. - 2018 ', '39e1f044-e27c-4d98-b123-58034f63cb09',
     'SERIES_PREF', 'Series B', 'Page 5 of 126\n'),
]


def get_ent_obj(v):
    return {
        "_id": v[1],
        "type": v[2].lower().replace('_', '-'),
        "value": v[3],
        "left": v[0],
        "right": v[4]
    }


somedict = {
    "entities": [get_ent_obj(c) for c in output]
}

jstr = json.dumps(somedict, ensure_ascii=False, indent=4)
print(jstr)
