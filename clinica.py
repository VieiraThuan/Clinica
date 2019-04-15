# clinica application
from odoo import models, fields

# Extend model
class Clinica_cadastro_paciente(models.Model):
	_inherit = 'res.partner'
	
	dt_nascimento = fields.Date("Data Nascimento")


class Clinica_cadastro_exame(models.Model):
	_name = 'exame.template'

	name = fields.Char("Nome do Exame")
	valor = fields.Float("Valor do Exame")
	descricao = fields.Text("Descrição")
	image_medium = fields.Binary("Medium-sized image", 
        help="Image of the exams (Medium-sized image of exame template if false).")
	ids_agendamento = fields.One2many('agenda_exame_template','id_exame')


class Clinica_agendamento_consulta(models.Model):
	_name = 'agenda_consulta_template'

	dt_consulta = fields.Datetime("Data da Consulta")
	name = fields.Many2one('res.partner','Paciente')
	nota = fields.Text("Notas")
	ids_exame = fields.One2many('agenda_exame_template','id_consulta')
	image_medium = fields.Binary("Medium-sized image", 
        help="Image of medical consultation (Medium-sized image of medical consultation template if false).")


class Clinica_agendamento_exame(models.Model):
	_name = 'agenda_exame_template'

	dt_exame = fields.Datetime("Data do Exame")
	id_consulta = fields.Many2one('agenda_consulta_template','Consulta')
	id_exame = fields.Many2one('exame.template','Exame')
	image_medium = fields.Binary("Medium-sized image", 
        help="Image of medical exam (Medium-sized image of medical exam template if false).")

