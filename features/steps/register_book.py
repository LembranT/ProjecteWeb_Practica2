import time
from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")


@when('I register book')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('boogeybookapp:book_create'))
        if context.browser.url == context.get_url('boogeybookapp:book_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for book by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from BoogeyBookAPP.models import BookRead
    book = BookRead.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(book)


@given('Exists book registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from BoogeyBookAPP.models import BookRead
    for row in context.table:
        book = BookRead(user=user)
        for heading in row.headings:
            setattr(book, heading, row[heading])
        book.save()


@when('I edit the book score with name "{name}"')
def step_impl(context, name):
    from BoogeyBookAPP.models import BookRead
    book = BookRead.objects.get(name=name)
    # Probablement petarà al enllaç
    context.browser.visit(context.get_url('/edit', book.pk))
    if context.browser.url == context.get_url('/edit', book.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()


@then('There are {count:n} book')
def step_impl(context, count):
    from BoogeyBookAPP.models import BookRead
    assert count == BookRead.objects.count()
