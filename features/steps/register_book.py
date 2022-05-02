from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")


@when('I register book')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('boogeybook:book_create'))
        if context.browser.url == context.get_url('boogeybook:book_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for book by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from BoogeyBookAPP.models import Reader
    restaurant = Reader.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(restaurant)


@then('There are {count:n} book')
def step_impl(context, count):
    from BoogeyBookAPP.models import Reader
    assert count == Reader.objects.count()
