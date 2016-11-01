# edc-readonly

View forms in read only mode. 

##Installation

    pip install git+https://github.com/botswana-harvard/edc-readonly.git
    
add to settings:
    
    INSTALLED_APPS = [
    ...
    'edc_readonly.apps.AppConfig',
    ...
    ]
    
## Usage

For a form that is to be shown on read only mode the following parameters are needed, `<app_label>`, `<model_name>`, `<form_module>`, `<form_class_str>`, `<pk>`.

    app_label - The app label of where the form and model is, e.g 'example'.
    model_name - The model that you want to show the from for, eg MyModel. 'example.MyModel' would be the app_name.model_name
    form_module - The module where the form class is, e.g 'example.forms'
    form_class_str - The from class name as an str, e.g 'MyModelForm'

The url to view the form in read only mode would be like this:

    <a href="{% url 'read_only_form_url' app_label my_model form_module form_class_str my_model_pk %}">browse data</a>

This will show the form fields that would show in admin but in read only mode, meaning the form fields will be read only and not editable.
