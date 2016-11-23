#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cgi
import urllib
import webapp2

from google.appengine.ext import ndb


class Student(ndb.Model):
    """Models an individual Guestbook entry with content and date."""
    snum = ndb.StringProperty()
    sname = ndb.StringProperty()
    sgrade = ndb.StringProperty()

    @classmethod
    def query_grade(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.sgrade)


class MainPage(webapp2.RequestHandler):
    def get(self):
        isAdmin = 0
        self.response.out.write(
            '<html><head><title>Score Query</title><style>body{text-align:center}</style></head><body>')
        snum = self.request.get('snum')
        if (snum == 'jiangtianyu2013223040202'):
            isAdmin = 1
        ancestor_key = ndb.Key("Record", snum or "*notitle*")
        students = Student.query_grade(ancestor_key).fetch(500)
        if (len(students) == 0):
            self.response.out.write('<blockquote>O(∩_∩)O~</blockquote>')
        else:
            for student in students:
                self.response.out.write('<blockquote>STUDENT ID: %s</blockquote>' %
                                        cgi.escape(student.snum))
                self.response.out.write('<blockquote>NAME: %s</blockquote>' %
                                        cgi.escape(student.sname))

                result = cgi.escape(student.sgrade).split('\t')
                self.response.out.write('<table border="1" align="center">')
                for r in result:
                    if (':' in r):
                        self.response.out.write(
                            '<tr><th>%s</th><td>%s</td></tr>' % (r.split(':')[0], r.split(':')[1]))
                    else:
                        self.response.out.write('<tr><td>%s</td></tr>' % r)
                self.response.out.write('</table><hr>')

        if (isAdmin == 1):
            self.response.out.write("""
            <hr>
              <form action="/sign?%s" method="post">
                <div><textarea name="sgrade" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Add Record"></div>
              </form>""" % urllib.urlencode({'snum': snum}))
        self.response.out.write("""
          <hr>
          <form>STUDENT ID: <input value="%s" name="snum">
          <input type="submit" value="GO"></form>
        </body>
      </html>""" % cgi.escape(snum))


class SubmitForm(webapp2.RequestHandler):
    def post(self):
        snum = self.request.get('snum')
        allscoredata = self.request.get('sgrade')
        scoredatalist = allscoredata.split('\n')
        for srecord in scoredatalist:
            student = Student(parent=ndb.Key("Record", srecord.split('\t', 2)[0] or "*notitle*"),
                              snum=srecord.split('\t', 2)[0],
                              sname=srecord.split('\t', 2)[1],
                              sgrade=srecord.split('\t', 2)[2])
            student.put()
        self.redirect('/?' + urllib.urlencode({'snum': snum}))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', SubmitForm)
])
