{
    'name': 'Hospital Management System',
    'version':'1.0',
    'author': 'Mohamed Abbes',
    'website': 'www.linkedin.com',
    'summary': 'A module for managing hospital operation',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/menu.xml',
        'views/patient.xml',
        'views/doctors.xml'
    ],
    'application':'True'
}
