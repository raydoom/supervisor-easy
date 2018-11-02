from Server import Server

SERVERS = [
    Server(
        name='90',
        host='192.168.0.90',
        port=9001,
        user='admin',
        password='admin'
    ),
    Server(
        name='33',
        host='192.168.0.33',
        port=9001,
        user='admin',
        password='admin'
    )
]

GROUPS = [
    {
        'name': 'all',
        'apps': ['33.tomcat701','90.ma']
    }
]


