def fetch_models():
    return ['Auctioned_item']


def build_home_context(context):
    context['models_list'] = fetch_models()

    return context
