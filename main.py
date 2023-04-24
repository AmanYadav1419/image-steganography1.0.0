from stegano import lsb

#hide messagae 

messagae = lsb.hide("minnie.png", "Hello world")
messagae.save('minnie.png')
print("done sir..")


secret_message = lsb.reveal("minnie.png")
print(secret_message)