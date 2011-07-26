# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import wizard
import decimal_precision as dp
import pooler
import time
from tools.translate import _
from osv import osv, fields
from tools.translate import _

class product_change_price(osv.osv_memory):
    _name = 'product.change.price'

    _columns ={
        'marchio':fields.many2one('marchio.marchio','Marchio',required=True),
        'categoria':fields.many2one('product.category','Categoria',required=True),
        'percentuale':fields.float('% di aumento o diminuzione',required=True),
    }

    def aggiorna(self, cr, uid, ids, context=None):
      #import pdb;pdb.set_trace()
      selezione_obj=self.pool.get('product.change.price').browse(cr,uid,ids)[0]
      Pro_obj = self.pool.get('product.product')
      templ_obj = self.pool.get('product.template')
      idsPro = Pro_obj.search(cr,uid,[('marchio_ids',"=",selezione_obj.marchio.id),('categ_id',"=",selezione_obj.categoria.id)])
      if idsPro:
        for Product in Pro_obj.browse(cr,uid,idsPro):
          Prezzo_nuovo = (Product.list_price*selezione_obj.percentuale/100)+Product.list_price
          templ_obj.write(cr,uid,Product. product_tmpl_id.id,{'list_price':Prezzo_nuovo})
          
        return {'type': 'ir.actions.act_window_close'}

product_change_price()





# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
