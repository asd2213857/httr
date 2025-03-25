def html_table_to_rows(table_soup, replace_str_list):
    rows = table_soup.find_all('tr')
    csv_rows = []
    for row in rows:
        csv_row = []
        if row.select("th,td"):
            for cell in row.select("th,td"):
                col_span = int(cell.get("colspan",1))
                cell_content = cell.text
                for replace_str in replace_str_list:
                    cell_content = cell_content.replace(replace_str, "")
                cell_content = cell_content.strip()
                csv_row+=[cell_content]*col_span
        if csv_row:
            csv_rows.append(csv_row)
    return csv_rows
