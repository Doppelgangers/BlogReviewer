class DataMixin():

    def get_context_data(self, **kwargs):
        context = kwargs
        context = super().get_context_data(**kwargs)
        context['title'] = 'Влог'
        return context