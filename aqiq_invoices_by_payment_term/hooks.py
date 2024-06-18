app_name = "aqiq_invoices_by_payment_term"
app_title = "Aqiq Invoices By Payment Term"
app_publisher = "Aqiq Solutions"
app_description = "Aqiq Invoices By Payment Term"
app_email = "info@aqiq.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aqiq_invoices_by_payment_term/css/aqiq_invoices_by_payment_term.css"
# app_include_js = "/assets/aqiq_invoices_by_payment_term/js/aqiq_invoices_by_payment_term.js"

# include js, css files in header of web template
# web_include_css = "/assets/aqiq_invoices_by_payment_term/css/aqiq_invoices_by_payment_term.css"
# web_include_js = "/assets/aqiq_invoices_by_payment_term/js/aqiq_invoices_by_payment_term.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "aqiq_invoices_by_payment_term/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "aqiq_invoices_by_payment_term/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "aqiq_invoices_by_payment_term.utils.jinja_methods",
#	"filters": "aqiq_invoices_by_payment_term.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "aqiq_invoices_by_payment_term.install.before_install"
# after_install = "aqiq_invoices_by_payment_term.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "aqiq_invoices_by_payment_term.uninstall.before_uninstall"
# after_uninstall = "aqiq_invoices_by_payment_term.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "aqiq_invoices_by_payment_term.utils.before_app_install"
# after_app_install = "aqiq_invoices_by_payment_term.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "aqiq_invoices_by_payment_term.utils.before_app_uninstall"
# after_app_uninstall = "aqiq_invoices_by_payment_term.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aqiq_invoices_by_payment_term.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"aqiq_invoices_by_payment_term.tasks.all"
#	],
#	"daily": [
#		"aqiq_invoices_by_payment_term.tasks.daily"
#	],
#	"hourly": [
#		"aqiq_invoices_by_payment_term.tasks.hourly"
#	],
#	"weekly": [
#		"aqiq_invoices_by_payment_term.tasks.weekly"
#	],
#	"monthly": [
#		"aqiq_invoices_by_payment_term.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "aqiq_invoices_by_payment_term.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "aqiq_invoices_by_payment_term.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "aqiq_invoices_by_payment_term.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["aqiq_invoices_by_payment_term.utils.before_request"]
# after_request = ["aqiq_invoices_by_payment_term.utils.after_request"]

# Job Events
# ----------
# before_job = ["aqiq_invoices_by_payment_term.utils.before_job"]
# after_job = ["aqiq_invoices_by_payment_term.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"aqiq_invoices_by_payment_term.auth.validate"
# ]
fixtures = [
    "Client Script",
    "Custom Field",
]