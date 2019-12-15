#!/usr/bin/env python2
#encoding: UTF-8
import json
#Name of the script used for the evalution
evaluation_script = 'ED'
#Custom evalution params
evaluation_params = json.loads("""{"SAMPLE_NAME_2_ID":"(?:word_)?([0-9]+).png","DOUBLE_QUOTES":true,"CRLF":false}""")
#Upload instructions
instructions = """<ul>
	<li>A single text file is expected.</li>
	<li>Each line of the submitted text file should follow the following format:&nbsp;<strong><em>#.png, &quot;transcription&quot;</em></strong>, where&nbsp;<strong><em>#.png</em></strong>&nbsp;refers to a word image of the test set, and the&nbsp;<em><strong>&quot;transcription&quot;</strong></em><strong>&nbsp;</strong>to the corresponding transcription.</li>
	<li>New lines in the text files should be indicated with the windows CR/LF termination.</li>
	<li>The double quote and backslash characters should be escaped as&nbsp;<strong><em>\&quot;</em></strong>&nbsp;and&nbsp;<em><strong>\\</strong></em>&nbsp;respectively.</li>
</ul>

<p>The submitted text file is automatically checked at the time of submission, and a submission log is presented to the user along with a confirmation of the submission. The checks performed are the following:</p>

<ul>
	<li>That the file submitted is a valid text file, it can be opened and read.</li>
	<li>That each line follows the format described above.</li>
	<li>That the word image numbers refered to are within the bounds of the test set.</li>
</ul>

<p>See here an example of the&nbsp;<a href="http://rrc.cvc.uab.es/files/task3_sample.txt">expected submission file</a></p>
"""
#Extension of the GT file. gt.[extension]
gt_ext = "txt"
#Acronym for the task. It's used to cache the Images
acronym = "IST-T3"
#Title of the Task
title = "Incidental Scene Text - Task 3 Word Recognition TEST DATASET (evaluation:Edit Distance)"
#Custom JavaScript for the visualiztion.
customJS = None
#Custom CSS for the visualiztion.
customCSS = None
#Parameters used to show the results of a method and the method's ranking
method_params = json.loads("""{"tedL":{"long_name":"Total Edit distance","type":"double","order":"asc","grafic":"2","format":""},"crw":{"long_name":"Correctly Recognised Words","type":"double","order":"desc","grafic":"1","format":"perc"},"tedupL":{"long_name":"T.E.D. (upper)","type":"double","order":"","grafic":"","format":""},"crwup":{"long_name":"C.R.W. (upper)","type":"double","order":"","grafic":"","format":"perc"}}""")
#Parameters to show for each sample
sample_params = json.loads("""{"edist":{"long_name":"Edit distance","type":"integer","order":"","grafic":"1","format":""},"norm":{"long_name":"Normalized","type":"double","order":"desc","grafic":"1","format":""},"edistUp":{"long_name":"E.D. (upper)","type":"integer","order":"","grafic":"2","format":""},"normUp":{"long_name":"Normalized (upper)","type":"double","order":"","grafic":"2","format":""},"gt":{"long_name":"GroundTruth","type":"string","order":"","grafic":"","format":""},"det":{"long_name":"Detection","type":"string","order":"","grafic":"","format":""}}""")
#Parameters to ask for for each submition
submit_params = json.loads("""{}""")
#Regular expression to get the Sample ID from the image name. ID must be the first capturing group.
image_name_to_id_str = 'word_([0-9]+).(jpg|gif|png)'
