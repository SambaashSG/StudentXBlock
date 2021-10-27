"""TO-DO: Write a description of what this XBlock is."""

import os
import pkg_resources
from django.template import Context

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String, Boolean
from xblockutils.resources import ResourceLoader
from django.contrib.auth.models import User


@XBlock.wants('user')
class StudentXBlock(XBlock):
    loader = ResourceLoader(__name__)

    display_name = String(
        display_name='Display Name',
        default='Online-Assessment',
        scope=Scope.settings,
        help='This name appears in the horizontal navigation at the top of the page.'
    )

    # fields
    url = String(
        display_name='Online-assessment Host URL',
        default='https://localhost:8080',
        scope=Scope.content,
        help='The URL for your Go to Online-Assessment.',
    )

    btnText = String(
        display_name='Button Text',
        default='Go To Assessment',
        scope=Scope.content,
        help='The text for Button text.',
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def render_template(self, path, context=None):
        """
        Evaluate a template by resource path, applying the provided context
        """

        return self.loader.render_django_template(os.path.join('static/html', path),
                                                  context=Context(context or {}),
                                                  i18n_service=self.runtime.service(self, 'i18n'))

    def student_view(self, request, context=None):
        """
        The primary view of the StudentXBlock, shown to students
        when viewing courses.
        """
        user_role = ""
        user_service = self.runtime.service(self, 'user')
        xb_user = user_service.get_current_user()
        print("USERID-------------------:", xb_user.opt_attrs.get('edx-platform.user_id'))
        user_id = xb_user.opt_attrs.get('edx-platform.user_id')
        user = User.objects.get(id=user_id)
        print("USER-----------------------:", user.is_superuser)
        if user.is_superuser:
            user_role = "learner_admin"
        elif user.is_staff:
            user_role = "assessor"

        context = {
            'url': self.url,
            'display_name': self.display_name,
            'button_text': self.btnText,
            'user_role': user_role
        }
        html = self.render_template("student_block_view.html", context)
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/student_block_view.css"))
        frag.add_javascript(self.resource_string("static/js/src/student_block_view.js"))
        frag.initialize_js('StudentBlockView')
        return frag

    # TO-DO: change this view to display your data your own way.
    def studio_view(self, context=None):
        context = {
            'display_name': self.display_name,
            'url': self.url,
            'button_text': self.btnText,
        }
        html = self.render_template("student_block.html", context)
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/student_block.js"))
        frag.initialize_js('StudentXBlock')
        return frag

    @XBlock.json_handler
    def save_student_value(self, data, suffix=''):
        self.display_name = data['display_name']
        self.url = data['host_url']
        self.btnText = data['btn_text']

        return {'result': 'success'}
