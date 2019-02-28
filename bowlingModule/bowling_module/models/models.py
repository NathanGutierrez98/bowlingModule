# -*- coding: utf-8 -*-
import base64
import re
from odoo import models, fields, api
from datetime import datetime
from openerp.osv import osv

class pista(models.Model):

     _name = 'bowling_module.pista'
     id_pista =  fields.Integer(string="Número pista",  required = True)
     estado = fields.Selection([('0','Desuso'),('1','Jugando')],string = "Estado de la pista")
     descripcion = fields.Text(string = "Notas de la pista")
     @api.one
     def cambiar_estado(self):
         if self.estado == '1':
             self.estado = '0'
         elif self.estado == '0':
             self.estado = '1'


     def get_estado(self):
         return self.estado
     _sql_constraints = [
         ('PK_ID_PISTA', 'unique (id_pista)','Ese id ya existe')]


class empleados(models.Model):

    _name = 'bowling_module.empleados'
    imagen = fields.Binary()
    id_empleado = fields.Char(string = "Numero de empleado", required = True)
    nombre = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string = "Apellidos", required = True)
    fecha_alta = fields.Date(string = "Alta del empleado", required = True, default = datetime.today())
    descripcion = fields.Text(string = "Notas del empleado")
    @api.onchange('id_empleado')
    def validate_dni(self):
        if self.id_empleado:
            match = re.match('[0-9]{8}[BCDFGHJKLMNPQRSTVXYZ]{1}$', self.id_empleado)
            if match == None:
                raise osv.except_osv(('Error'), ('NO ES UN DNI VALIDO'))
    _sql_constraints = [
         ('PK_ID_EMPLE', 'unique (id_empleado)','ESE DNI YA EXISTE')]




class jugador(models.Model):
    _name = 'bowling_module.jugador'
    nombre = fields.Char(string = "Nombre de jugador", required = True)
    pie = fields.Integer(string = "Numero de pie", required = True)


class mantenimiento(models.Model):
    _name = 'bowling_module.mantenimiento'
    pista = fields.Many2many('bowling_module.pista', 'id_pista', string='Pista', required = True)
    empleados = fields.Many2many('bowling_module.empleados', 'id_empleado', string='Empleado', required = True)
    fecha_mantenimiento = fields.Date(string = " Fecha mantenimiento ",required = True, default = datetime.today())
    descripcion = fields.Text(string = "Notas de mantenimiento")



class partidas(models.Model):
    _name = 'bowling_module.partidas'
    pista = fields.Many2many('bowling_module.pista')

    jugador = fields.Many2many('bowling_module.jugador')
    fecha_partida = fields.Date(string = "Fecha de partida", required = True, default = datetime.today())
    precio = fields.Selection([('0','4.50'),('1','3.50')],string = "Precio", default = '0')
    importe_total = fields.Float(compute = "calcular_importe", store = True)

    @api.model
    def create(self, vals):
        rec = super(partidas, self).create(vals)
        if rec.pista.get_estado() == '0':
            rec.pista.cambiar_estado()
        else:
            raise osv.except_osv(('Error'), ('Error la pista ya está en uso'))

        return rec




    @api.depends('precio','jugador')
    def calcular_importe(self):
        for r in self:
            r.importe_total = float(dict(self._fields['precio'].selection).get(self.precio)) * len(r.jugador)
