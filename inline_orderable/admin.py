from django.contrib.admin import TabularInline, StackedInline


class OrderableStackedInline(StackedInline):
    class Media:
        js = ('inline_orderable/inline_orderable.js', 'inline_orderable/stackedinline_orderable.js',)


class OrderableTabularInline(TabularInline):    
    class Media:
        js = ('inline_orderable/inline_orderable.js', 'inline_orderable/tabularinline_orderable.js',)