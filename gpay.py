import gp

jd=gp.Google_pay("jeyadevl@gmail.com","8667633927","Jeyadev L")
jd.open_gpay()
jd.email_verification()
jd.mobile_verification()
jd.name_verification()
jd.otp_verification(15698,15698)
jd.Bank_verification()
jd.PanCard_Verification()
jd.set_Pin("5384")
jd.Enter_your_Pin(3465,3465)

class Phone_pe(gp.Google_pay):                                                                                          #INHERITANCE
    def __init__(slef,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")
        
jd1=Phone_pe("jeyadevl@gmail.com","8667633927","Jeyadev L")
jd1.open_phonepe()
jd1.mobile_verification()
jd1.name_verification()
jd1.otp_verification(780965,780965)
jd1.Bank_verification()
jd1.PanCard_Verification()
jd1.set_Pin("238790")
jd1.Enter_your_Pin(3564,3564)


        
googlepay=[{"name":"abishek","gpaynum":7397266887,"type":"personal","transaction":"regular"},                       #DICTIONARY INSIDE LIST
           {"name":"aarthi","gpaynum":7305341565,"type":"personal","transaction":"regular"},
           {"name":"abinaya","gpaynum":6381347949,"type":"personal","transaction":"rare"},
           {"name":"afrin","gpaynum":7358355054,"type":"personal","transaction":"never"},
           {"name":"ajay","gpaynum":7200636126,"type":"personal","transaction":"rare"},
           {"name":"ahmed","gpaynum":9597916931,"type":"personal","transaction":"rare"},
           {"name":"athai","gpaynum":8056469214,"type":"personal","transaction":"regular"},
           {"name":"anandh","gpaynum":9962454833,"type":"personal","transaction":"rare"},
           {"name":"anandhi","gpaynum":8015341851,"type":"personal","transaction":"rare"},
           {"name":"angamma","gpaynum":7305624091,"type":"personal","transaction":"rare"},
           {"name":"anitha","gpaynum":8939509826,"type":"personal","transaction":"rare"},
           {"name":"archana","gpaynum":6369121983,"type":"personal","transaction":"regular"},
           {"name":"ashwini","gpaynum":9833807044,"type":"personal","transaction":"regular"},
           {"name":"asma","gpaynum":9941297487,"type":"personal","transaction":"rare"},
           {"name":"bagavathi","gpaynum":7200001990,"type":"personal","transaction":"regular"},
           {"name":"balaji","gpaynum":6382880108,"type":"personal","transaction":"rare"},
           {"name":"belgin","gpaynum":9941656319,"type":"personal","transaction":"regular"},
           {"name":"beulah","gpaynum":9500075619,"type":"personal","transaction":"rare"},
           {"name":"bhuvan","gpaynum":8072512570,"type":"personal","transaction":"regular"},
           {"name":"chandru","gpaynum":6382761961,"type":"personal","transaction":"rare"},
           {"name":"chipe","gpaynum":9791045340,"type":"personal","transaction":"regular"},
           {"name":"deen","gpaynum":9841032642,"type":"personal","transaction":"regular"},
           {"name":"deepa","gpaynum":6383908036,"type":"personal","transaction":"regular"},
           {"name":"dharan","gpaynum":8248631340,"type":"personal","transaction":"rare"},
           {"name":"divya","gpaynum":6374339918,"type":"personal","transaction":"regular"},
           {"name":"doss","gpaynum":9840644601,"type":"personal","transaction":"regular"},
           {"name":"durka","gpaynum":6379741175,"type":"personal","transaction":"regular"},
           {"name":"esther","gpaynum":8124252926,"type":"personal","transaction":"regular"},
           {"name":"femila","gpaynum":9176093745,"type":"personal","transaction":"regular"},
           {"name":"gautam","gpaynum":9176358088,"type":"personal","transaction":"regular"},
           {"name":"gayathri","gpaynum":7305331140,"type":"personal","transaction":"rare"},
           {"name":"gomathi","gpaynum":6384316771,"type":"personal","transaction":"regular"},
           {"name":"gracy","gpaynum":9150381712,"type":"personal","transaction":"regular"},
           {"name":"grishma","gpaynum":9003037517,"type":"personal","transaction":"regular"},
           {"name":"hari","gpaynum":9515605233,"type":"personal","transaction":"regular"},
           {"name":"haripriya","gpaynum":9791143754,"type":"personal","transaction":"regular"},
           {"name":"harikrishnan","gpaynum":8056265597,"type":"personal","transaction":"regular"},
           {"name":"hema","gpaynum":7010469081,"type":"personal","transaction":"regular"},
           {"name":"indumathi","gpaynum":6379840455,"type":"personal","transaction":"rare"},
           {"name":"jaya","gpaynum":9791280444,"type":"personal","transaction":"regular"},
           {"name":"jayadev","gpaynum":8667639927,"type":"personal","transaction":"rare"},
           {"name":"jeevitha","gpaynum":8667464628,"type":"personal","transaction":"regular"},
           {"name":"jemima","gpaynum":9962821791,"type":"personal","transaction":"regular"},
           {"name":"jes","gpaynum":9551852580,"type":"personal","transaction":"rare"},
           {"name":"jesintha","gpaynum":8939475795,"type":"personal","transaction":"regular"},
           {"name":"jo","gpaynum":7338935895,"type":"personal","transaction":"rare"},
           {"name":"joel","gpaynum":9444919116,"type":"personal","transaction":"regular"},
           {"name":"jonnah","gpaynum":8531025248,"type":"personal","transaction":"regular"},
           {"name":"josh","gpaynum":9789869415,"type":"personal","transaction":"regular"},
           {"name":"jothika","gpaynum":9677150962,"type":"personal","transaction":"regular"},
           {"name":"julaika","gpaynum":9003899016,"type":"personal","transaction":"rare"},
           {"name":"jv","gpaynum":9361486028,"type":"personal","transaction":"regular"},
           {"name":"kamali","gpaynum":6382826039,"type":"personal","transaction":"regular"},
           {"name":"kamini","gpaynum":9080995159,"type":"personal","transaction":"regular"},
           {"name":"kani","gpaynum":8220584872,"type":"personal","transaction":"rare"},
           {"name":"kannan","gpaynum":9710405288,"type":"personal","transaction":"rare"},
           {"name":"karthi","gpaynum":8778799456,"type":"personal","transaction":"regular"},
           {"name":"kavitha","gpaynum":9840042296,"type":"personal","transaction":"regular"},
           {"name":"keerthi","gpaynum":7305066119,"type":"personal","transaction":"rare"},
           {"name":"kingsley","gpaynum":8754554295,"type":"personal","transaction":"regular"},
           {"name":"kiran","gpaynum":6383634327,"type":"personal","transaction":"rare"},
           {"name":"kiruthika","gpaynum":9789029339,"type":"personal","transaction":"regular"},
           {"name":"kowsalya","gpaynum":7871125838,"type":"personal","transaction":"regular"},
           {"name":"kowsi","gpaynum":7448744931,"type":"personal","transaction":"rare"},
           {"name":"kumar","gpaynum":7358565943,"type":"personal","transaction":"regular"},
           {"name":"lekha","gpaynum":7305772128,"type":"personal","transaction":"regular"},
           {"name":"lokesh","gpaynum":7358479530,"type":"personal","transaction":"regular"},
           {"name":"monisha","gpaynum":6383188073,"type":"personal","transaction":"regular"},
           {"name":"madhan","gpaynum":9940235467,"type":"personal","transaction":"rare"},
           {"name":"madhumitha","gpaynum":7358602342,"type":"personal","transaction":"regular"},
           {"name":"madhuri","gpaynum":9500771102,"type":"personal","transaction":"regular"},
           {"name":"maha","gpaynum":9092042867,"type":"personal","transaction":"regular"},
           {"name":"maheswari","gpaynum":9445891948,"type":"personal","transaction":"regular"},
           {"name":"malathi","gpaynum":8754348244,"type":"personal","transaction":"rare"},
           {"name":"manni","gpaynum":7395949407,"type":"personal","transaction":"regular"},
           {"name":"mannjula","gpaynum":9751783763,"type":"personal","transaction":"regular"},
           {"name":"manoj","gpaynum":7358160847,"type":"personal","transaction":"regular"},
           {"name":"mathu","gpaynum":7550228649,"type":"personal","transaction":"regular"},
           {"name":"megna","gpaynum":9620423983,"type":"personal","transaction":"rare"},
           {"name":"mohan","gpaynum":8526264054,"type":"personal","transaction":"rare"},
           {"name":"moideen","gpaynum":6381281050,"type":"personal","transaction":"regular"},
           {"name":"mrithula","gpaynum":9840696542,"type":"personal","transaction":"regular"},
           {"name":"muthu","gpaynum":8124263483,"type":"personal","transaction":"regular"},
           {"name":"mythili","gpaynum":63830035506,"type":"personal","transaction":"regular"},
           {"name":"nabisha","gpaynum":9094639197,"type":"personal","transaction":"regular"},
           {"name":"nivetha","gpaynum":9150544355,"type":"personal","transaction":"rare"},
           {"name":"nourin","gpaynum":7806906745,"type":"personal","transaction":"regular"},
           {"name":"padma","gpaynum":9150961045,"type":"personal","transaction":"regular"},
           {"name":"panisha","gpaynum":9676520865,"type":"personal","transaction":"regular"},
           {"name":"parimala","gpaynum":7358470300,"type":"business","transaction":"rare"},
           {"name":"parveen","gpaynum":8838105667,"type":"personal","transaction":"regular"},
           {"name":"pavithra","gpaynum":6369772429,"type":"personal","transaction":"regular"},
           {"name":"philip","gpaynum":9790830981,"type":"personal","transaction":"regular"},
           {"name":"pinky","gpaynum":9489300189,"type":"personal","transaction":"regular"},
           {"name":"pooja","gpaynum":8610129526,"type":"personal","transaction":"regular"},
           {"name":"prathi","gpaynum":7397347695,"type":"personal","transaction":"rare"},
           {"name":"praveen","gpaynum":9500079580,"type":"personal","transaction":"regular"},
           {"name":"preethi","gpaynum":7708374654,"type":"personal","transaction":"regular"},
           {"name":"prem","gpaynum":9344028505,"type":"personal","transaction":"regular"},
           {"name":"priya","gpaynum":6369143345,"type":"personal","transaction":"rare"},
           {"name":"ragul","gpaynum":9894190843,"type":"personal","transaction":"regular"},
           {"name":"rajesh","gpaynum":7401790602,"type":"personal","transaction":"regular"},
           {"name":"ramya","gpaynum":9840430478,"type":"personal","transaction":"regular"},
           {"name":"regina","gpaynum":9840860014,"type":"personal","transaction":"rare"},
           {"name":"reshma","gpaynum":7448729790,"type":"personal","transaction":"regular"},
           {"name":"rohini","gpaynum":6380874698,"type":"personal","transaction":"rare"},
           {"name":"sabitha","gpaynum":9361447138,"type":"personal","transaction":"regular"},
           {"name":"sagarika","gpaynum":7358701090,"type":"personal","transaction":"regular"},
           {"name":"sameera","gpaynum":6382718022,"type":"personal","transaction":"regular"},
           {"name":"sandhiya","gpaynum":6383138140,"type":"personal","transaction":"rare"},
           {"name":"sangeetha","gpaynum":7904104077,"type":"personal","transaction":"regular"},]


for i in googlepay:                                                                                                             #LOOPING
    for j,k in i.items():                                                                                                       #KEY VALUES LOOPING
        print(f"{j}:{k}")
    
