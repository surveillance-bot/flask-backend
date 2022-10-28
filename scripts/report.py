from reportlab.pdfgen import canvas
 
def create_pdf():
    
    dic = [
        ['8cf7ba07-56bd-11ed-bdaa-005056c00008', [
        {
            'location': "2hhhsshhhhz2",
            'time': "12:22pm",
            'date': "12/12/12"
        },{
            'location': "zjjjzjzzj",
            'time': "2:22am",
            'date': "12/1/10"
        },{
            'location': "2zshdzjzdj2",
            'time': "1:20pm",
            'date': "17/2/12"
        }
        ]],
        
        ['83cf2712-56bd-11ed-a2ab-005056c00008', [
        {
            'location': "22",
            'time': "12:22pm",
            'date': "12/12/12"
        },{
            'location': "22",
            'time': "12:22pm",
            'date': "12/12/12"
        },{
            'location': "22",
            'time': "12:22pm",
            'date': "12/12/12"
        }
        ]],
        
        ['86654eab-56bd-11ed-aef6-005056c00008', [
        {
            'location': "22",
            'time': "12:22pm",
            'date': "12/12/12"
        },{
            'location': "22",
            'time': "12:22pm",
            'date': "12/12/12"
        },{
            'location': "22",
            'time': "12:22pm",
            'date': "12/12/12"
        }
        ]]
    ]

    pdf_file = 'report.pdf' 
    can = canvas.Canvas(pdf_file)
    
    for i in range(0, len(dic)):
        img_file = "C:/Users/daksh/Desktop/VSCode/SurveillanceBot/flask-backend/imfaces/" + dic[i][0] + '.jpg'
        can.drawImage(img_file, 40, 700, width=100)
        
        for j in range(0, len(dic[i][1])):
            can.drawString(40, 650 - 50*j, "Location: " + dic[i][1][j]["location"])
            can.drawString(40, 640 - 50*j, "Time: " + dic[i][1][j]["time"])
            can.drawString(40, 630 - 50*j, "Date: " + dic[i][1][j]["date"])

        can.showPage()
    can.save()
 
create_pdf()