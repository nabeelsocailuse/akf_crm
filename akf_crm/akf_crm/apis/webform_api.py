import frappe

@frappe.whitelist(allow_guest=True)
def get_filtered_programs(**filters: dict):
	gender = filters.get("gender")
	institute = filters.get("institute")
	intended_level_of_study = filters.get("intended_level_of_study")
	preferred_city = filters.get("preferred_city")
	query = """
			Select (program_name) as value, (program_name) as text
			From `tabProgram`
			Where docstatus=0
	"""
	if(gender): 
		query += f" and gender in ('', '{gender}') "
	if(institute):	
		query += f" and institute = '{institute}' "
	if(intended_level_of_study):	
		query += f" and intended_level_of_study = '{intended_level_of_study}' "
	if(preferred_city):	
		query += f" and preferred_city = '{preferred_city}' "
	
	return frappe.db.sql(query, as_dict=1)

@frappe.whitelist(allow_guest=True)
def get_proposed_program_of_study(program_name,**filters: dict):
	# program_name = filters.get("program_name")
	if(program_name):
		return frappe.db.sql(f"""
				Select name
				From `tabProgram`
				Where docstatus=0
				and program_name = '{program_name}'
		""")[0][0] or None
	return None
#  bench --site erp.palestinescholarship.org execute akf_crm.akf_crm.apis.webform_api.update
def update():
	print(frappe.translate.get_user_language())
	# for d in  frappe.db.get_list('CRM Lead', filters={'proposed_program_of_study': ["is", "not set"]}, fields=['name', 'select_field_study_program']):
	# 	print(f'---> {d.select_field_study_program}')
	# 	pid = get_proposed_program_of_study(d.select_field_study_program)
	# 	print(f'{pid}')
	# 	frappe.db.set_value('CRM Lead', d.name, 'proposed_program_of_study', pid, update_modified=False)