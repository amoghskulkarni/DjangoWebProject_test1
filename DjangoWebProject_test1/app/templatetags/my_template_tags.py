from django import template

def give_filename_from_path (value):
    names = value.split('/')
    return names[-1]

register = template.Library()

register.filter('giveFilename', give_filename_from_path)