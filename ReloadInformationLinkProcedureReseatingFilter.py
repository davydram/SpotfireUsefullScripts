''' Author			: Davyd Ramos
	Date Created	: 05.18.2023  
	Description		: Reloads the data from the Get Store Procedures when the users select a single
					  study in the input screen and click on reload button.
	
	
	Modification Log
	Date        Intial  Reference    Comment
	----------  ------  -----------  ----------------------------------------------------------
	04.30.2024   DR     TASK-241     CREATED
						TASK-237	 created information link
						TASK-280	 created information link
						TASK-6171  	 created information link
						TASK-6173 	 created information link
						TASK-6178 	 created information link
									 created information link
						TASK-6633 	 replaced/comented created information link 
	
	__________   ___    _______________________________________________________________________	
	__________   ___    _______________________________________________________________________	

'''
#TASK-6633

#Get a list of tables from the active page
tg = Document.ActivePageReference.FilterPanel.TableGroups


#Show available filters
print "Available filters:"
for t in tg:
 print t
print "------------\n"

#See if a filter is available on the filter panel
print "Visibility of filters in a table group"
for h in tg[0].FilterHandles:
 print h.FilterReference.Name, h.Visible
print "------------\n"

#Reset all available filters
print "Print all available filters and reset only the visible ones"
for t in tg:
 for h in t.FilterHandles:
   f = h.FilterReference

   #print available filters (and visibility status)
   print '[',t,'].[',f.Name,'].Visible = ',h.Visible

   #reset the filter only if it's visible
   if (h.Visible): f.Reset()

#Start Load data tables:

print "Start Loading"

Document.Data.Tables['AnalysisReference'].ReloadAllData() 
Document.Data.Tables['IL_SP_ProjectionBackup'].ReloadAllData()  
Document.Data.Tables['IL_SP_FinishedReport'].ReloadAllData()   
Document.Data.Tables['IL_SP_CurrentBackup'].ReloadAllData() 		
Document.Data.Tables['IL_SP_ExpensesBackup'].ReloadAllData() 			
Document.Data.Tables['IL_SP_Expenses'].ReloadAllData()	 
Document.Data.Tables['IL_SP_AnalysisRaw'].ReloadAllData() 	
Document.Data.Tables['IL_SP_PlanningBackup'].ReloadAllData() 
Document.Data.Tables['IL_SP_AnalysisDetailed'].ReloadAllData() 
Document.Data.Tables['IL_SP_AnalysisBackup'].ReloadAllData() 
Document.Data.Tables['IL_SP_VisitSummayReports'].ReloadAllData()  #TASK-237
#Document.Data.Tables['IL_SP_SiteSummary'].ReloadAllData() #TASK-280 
Document.Data.Tables['IL_SP_SubjectBasedPass-Thru'].ReloadAllData() #TASK-6171 
Document.Data.Tables['IL_SP_OtherReimbursable'].ReloadAllData() #TASK-6173 
Document.Data.Tables['IL_SP_Sunburst'].ReloadAllData() 	 #TASK-6178 
Document.Data.Tables['IL_SP_SunburstDetail'].ReloadAllData() #TASK-6178 
Document.Data.Tables['IL_SP_SiteSummary'].ReloadAllData() #TASK-6633 

#End Loads:
print "End Loading"
