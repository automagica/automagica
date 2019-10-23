
def insert_table_header(data):
    """
    Inserts the header of an Automagica Report.
    """
    data_keys = []

    for row in data:
        for key, _ in row.items():
            if key not in data_keys:
                data_keys.append(key)

    header = '|'.join(data_keys)

    header_next = '|'.join(['---' for key in data_keys])
    
    print('AUTOMAGICA_MARKDOWN_START: ' + str(header) + ' :AUTOMAGICA_MARKDOWN_END')
    print('AUTOMAGICA_MARKDOWN_START: ' + str(header_next) + ' :AUTOMAGICA_MARKDOWN_END')

    return data_keys


def insert_table_item(item, keys):
    """
    Inserts the header of an Automagica Report.
    """
    print('AUTOMAGICA_MARKDOWN_START: ' + '|'.join([str(item.get(key, '')) for key in keys]) + ' :AUTOMAGICA_MARKDOWN_END')

 
def insert_table(data):
    '''
    Function to report in the Automagica Portal. Can be used to generate reports, 
    logs and worklists. Only available to users with access to the Portal. 
    This outputs a list of flat dicts to a markdown table with headers to the console.
    '''
    keys = insert_table_header(data)

    for item in data:
        insert_table_item(item, keys)


def insert_title(title='My title', level=1):
    '''
    Function to insert a report title in the Automagica Portal.
    This outputs a string as a title to the console.
    '''
    print('AUTOMAGICA_MARKDOWN_START: ' + '#' * level + ' :AUTOMAGICA_MARKDOWN_END')


