def fetch_models():
    return ['Employee', 'Maintanence', 'Payment', 'Division']


def build_home_context(context):
    context['models_list'] = fetch_models()

    return context
