import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):   #这是一个测试用类，它继承了xxx
    '''针对AnonymousSurvey类的测试'''

    def test_store_single_response(self):
        '''测试单个答案会被妥善地存储'''
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)   #创建了一个实例
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)   #assertIn(a, b)表示断言字符串a在列表b中

    def test_store_three_responses(self):
        '''测试三个答案会被妥善地存储'''
        question = 'What language did you first learn to speak?'''
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)
            

unittest.main( )
