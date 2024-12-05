# -*- coding: utf-8 -*-
from odoo import http


class ListaTareas(http.Controller):
    @http.route('/lista_tareas/lista_tareas', auth='public')
    def index(self, **kw):
        print("Hola Mundo, DAM2")

    @http.route('/lista_tareas/lista_tareas/objects', auth='public')
    def list(self, **kw):
        return http.request.render('lista_tareas.listing', {
            'root': '/lista_tareas/lista_tareas',
            'objects': http.request.env['lista_tareas.lista_tareas'].search([]),
        })

    @http.route('/lista_tareas/lista_tareas/objects/<model("lista_tareas.lista_tareas"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('lista_tareas.object', {
            'object': obj
        })
    @http.route('/lista_tareas/lista_tareas/listado', type='http', auth='public', methods=['GET'])
    def listado_tareas(self, **kw):
        tareas = request.env[('lista_tareas.lista_tareas')].search([])
        tareas_list = []
        for tarea in tareas:
            tareas_list.append({
                'id': tarea.id,
                'tarea': tarea.tarea,
                'prioridad': tarea.prioridad,
                'urgente': tarea.urgente,
                'realizada': tarea.realizada,
            })

        return request.make_response(
            json.dumps(tareas_list),
            header={'Content-Type': 'application/json'}
        )

