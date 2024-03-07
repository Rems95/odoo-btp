from odoo import fields, models

class Client(models.Model):
    _name = "reception.client"
    _description = "Client"

    nom = fields.Char("Nom", required=True)
    prenom = fields.Char("Prenom", required=True)
    