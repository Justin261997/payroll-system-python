# -*- coding: utf-8 -*-

def designations():
    desform=SQLFORM.smartgrid(db.designation,deletable=True,editable=True,ui='web2py',user_signature=False)
    return locals()
def employees():
    empform=SQLFORM.smartgrid(db.employee,deletable=True,editable=True,ui='web2py',user_signature=False)
    return locals()
def leaves():
    lveform=SQLFORM.smartgrid(db.lve,deletable=True,editable=True,ui='web2py',user_signature=False)
    return locals()
def pbr():
    pbrform=SQLFORM.smartgrid(db.pbr,deletable=True,editable=True,ui='web2py',user_signature=False)
    return locals()
def remitence():
    remform=SQLFORM.smartgrid(db.remitence,deletable=True,editable=True,ui='web2py',user_signature=False)
    return locals()
def bank():
    bankform=SQLFORM.smartgrid(db.bank,deletable=True,editable=True,ui='web2py',user_signature=False)
    return locals()
