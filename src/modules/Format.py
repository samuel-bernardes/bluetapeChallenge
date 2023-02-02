class Format():

    def style(writer, df):
        workbook = writer.book
        worksheet = writer.sheets['report']

        worksheet.set_zoom(90)
        header_format = workbook.add_format({
            "valign": "vcenter",
            "align": "center",
            "bg_color": "#1EDDFA",
            "bold": True,
            "font_color": "#FFFFFF"
        })

        title = "Resultado: Busca de palavras por site"

        format = workbook.add_format()
        
        format.set_font_size(20)
        format.set_font_color("#333333")

        subtitle = "Número de ocorrência de palavras por site"
        worksheet.merge_range('A1:AS1', title, format)
        worksheet.merge_range('A2:AS2', subtitle)
        worksheet.set_row(2, 15)

        for col_num, value in enumerate(df.columns.values):
            worksheet.write(2, col_num, value, header_format)

        worksheet.set_column("A:A", 140)
        worksheet.set_column("B:C", 30)

        writer.close()
