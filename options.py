from PyQt5.QtCore import QTime

win_width = 1850
win_height = 1300
pulse_icon = 'pulse.png'
win_title = 'Rufier-test - by Alen Jumayev and Olzhas Amankeldin'
hello = 'Welcome to the health assessment program!'
txt_instruction = 'This application will allow you to use the Rufier test to conduct a primary ' \
                  'diagnosis of your health.\n' \
                  'The Rufier test is a load complex designed to assess performance ' \
                  'hearts during physical exertion.\n' \
                  'The pulse rate is determined in the subject who is lying on his back for 5 ' \
                  'minutes in 15 seconds;\n' \
                  'then, within 45 seconds, the subject performs 30 squats.\n' \
                  'After the end of the load, the subject lies down, and the number of pulsations ' \
                  'for him is counted again.' \
                  'the first 15 seconds,\n' \
                  'and then — for the last 15 seconds of the first minute of the recovery period.\n' \
                  'Important! If you feel unwell during the test\n' \
                  '(dizziness will appear, tinnitus, severe shortness of breath, etc.)\n' \
                  'then the test should be interrupted and consult a doctor.'
button_next = 'Next'
name = 'Write your full name: '
age = 'Age: '
test1 = 'Lie on your back and measure your pulse in 15 seconds. ' \
        'Click the "Start First Test" button to start the timer '\
        'Write the result in the appropriate field.'
test2 = 'Perform 30 squats in 45 seconds. ' \
        'To do this, click the "Start doing squats" button to start the squat counter.'
test3 = 'Lie on your back and measure your pulse first for the first 15 seconds of the minute, ' \
        'then in the last 15 seconds. ' \
        'Click the "Start Final test" button, to start the timer.\n' \
        'Green indicates the seconds during which it is necessary\n' \
        'take measurements, black - seconds without measuring pulsations. ' \
        'Write down the results in the appropriate fields.'
time = QTime(0, 0, 15)
timer = time.toString("hh:mm:ss")
hintname = "Full name"
hintage = "0"
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_finalwin = 'Results'
rufieindex = 'Rufier Index:'
txt_workheart = 'Heart health: '
txt_res1 = "low. Urgently address to the doctor!"
txt_res2 = "Satisfactory. See a doctor!"
txt_res3 = "Medium. May need to see a doctor."
txt_res4 = "above average"
txt_res5 = "high"