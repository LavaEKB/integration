from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATE_DIR = "/home/lava/Рабочий стол/Work/integration/integration/templates" 
#print(TEMPLATE_DIR)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'integration', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


print(TEMPLATES[0]['DIRS'])