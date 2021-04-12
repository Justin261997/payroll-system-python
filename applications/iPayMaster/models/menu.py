# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
                  (T('Home'), False, URL('default', 'index'), []),
                  (T('Manage Employee'),True,'#',[
											        (T('Add Employee'),False,URL('form','employees/employee/new/employee'),[]),
                                                    (T('Signup User'),False,URL('form','signup'),[]),
                                                    (T('View Employee'),False,URL('form','employees'),[]),
											      ]),
				  (T('Manage Leave'),True,'#',[
				                                    (T('View Leave History'),False,URL('form','leaves'),[]),
											        (T('Apply for leave'),False,URL('form','leaves/lve/new/lve'),[]),
										       ]),
				  (T('Manage Salary'),True,'#',[
				                                    (T('View Salary Details'),False,URL('form','salaries'),[]),
											        (T('View Salary History'),False,URL('form','salaryhistories'),[]),
											        (T('View Bank Details'),False,URL('form','bank'),[]),
										            (T('Manage Remitence'),False,URL('form','remitence'),[]),
   										        ]),
				  (T('Other'),True,'#',[
				                                    (T('Designation Details'),False,URL('form','designations'),[]),
											        (T('Status'),False,URL('form','statuses'),[]),
											        (T('Salaryheads'),False,URL('form','salaryheads'),[]),
								       ]),
                  (T('Process'),True,'#',[
                                                    (T('Add Salary'),False,URL('form','salaryhistories/salaryhistory/new/salaryhistory')),
				                                    (T('Generate Pay Bill'),False,URL('form','paybillgenerator'),[]),
                                                    (T('View Bills'),False,URL('form','viewbills'),[]),
								         ]),
                  (T('Salary history'), False, URL('process', 'salaryhistory'), [])

                ]

response.pmenu = [
                  (T('Home'), False, URL('default', 'index'), []),
                  (T('View bills'),False, URL('form', 'pviewbills'), []),
                  (T('View leave requests'),False, URL('form', 'pviewleave'), []),

                ]

response.emenu = [
                  (T('Home'), False, URL('default', 'index'), []),
                  (T('Apply for leave'),False,URL('form','applylve'), []),
                  (T('Leave History'),False,URL('form','eviewleave'), []),

                 ]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += []
