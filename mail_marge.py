# python program to mail marger
# names are in file names.txt
#body of the mail is in body.txt

#open names.txt for reading
with open("names.txt", 'r', encoding= 'utf-8') as names_files:

    #open body.txt for reading
    with open("body.txt", 'r', encoding = 'utf-8') as body_files:

        #read entire content of file
        body = body_files.read()

        #iterate over names
        for name in names_files:
            mail = "Hello " + name.strip() + "\n" + body

            #write the mails to individual files
            with open(name.strip()+ ".txt", 'w', encoding ='utf-8') as mail_file:
                mail_file.write(mail)