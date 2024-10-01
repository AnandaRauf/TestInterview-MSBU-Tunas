from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MasterRuangan(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    name = fields.Char('Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('kecil', 'Meeting Room Kecil'),
        ('besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    lokasi_ruangan = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')
    ], string='Lokasi Ruangan', required=True)
    foto_ruangan = fields.Binary('Foto Ruangan', required=True)
    kapasitas_ruangan = fields.Integer('Kapasitas Ruangan', required=True)
    keterangan = fields.Text('Keterangan')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Nama Ruangan tidak boleh sama.')
    ]


class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'
    
    nomor_pemesanan = fields.Char('Nomor Pemesanan', readonly=True, required=True, copy=False, default='New')
    ruangan_id = fields.Many2one('master.ruangan', string='Ruangan', required=True)
    nama_pemesan = fields.Char('Nama Pemesan', required=True)
    tanggal_pemesanan = fields.Date('Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], string='Status Pemesanan', default='draft', required=True)
    catatan_pemesanan = fields.Text('Catatan Pemesanan')

    @api.model
    def create(self, vals):
        # Generate Nomor Pemesanan
        if vals.get('nomor_pemesanan', 'New') == 'New':
            vals['nomor_pemesanan'] = self.env['ir.sequence'].next_by_code('pemesanan.ruangan') or 'New'
        return super(PemesananRuangan, self).create(vals)

    @api.constrains('ruangan_id', 'tanggal_pemesanan')
    def _check_pemesanan_unik(self):
        for record in self:
            existing_booking = self.env['pemesanan.ruangan'].search([
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id)
            ])
            if existing_booking:
                raise ValidationError("Tidak boleh memesan ruangan dan tanggal pemesanan yang sama.")

    _sql_constraints = [
        ('unique_nama_pemesan', 'unique(nama_pemesan)', 'Nama Pemesan tidak boleh sama.')
    ]

    def action_set_ongoing(self):
        self.write({'status_pemesanan': 'ongoing'})

    def action_set_done(self):
        self.write({'status_pemesanan': 'done'})
