{
    'name': 'Room Management',
    'version': '1.0',
    'category': 'Operations',
    'description': """
        Modul untuk mengelola pemesanan ruangan, termasuk master ruangan dan pemesanan ruangan.
    """,
    'author': 'Senior System Engineer',
    'depends': ['base'],
    'data': [
    'data/data_sequence.xml',  # Tambahkan ini untuk memuat file sequence
    'views/ruangan_views.xml',
    'views/pemesanan_views.xml',
],

    'installable': True,
    'application': True,
}
