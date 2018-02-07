import os
from django.template import Template


def get_template(template_filename):
    filename = os.path.dirname(os.path.realpath(__file__)) + "/templates/" + template_filename
    filehandle = open(filename, "r")
    file_contents = filehandle.read()
    filehandle.close()
    return Template(file_contents)
