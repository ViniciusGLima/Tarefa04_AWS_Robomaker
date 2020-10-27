import rospy

from std_msgs.msg import String


rospy.init_node('no_matricula')

resultado_soma = String()

def sub_matriculaCallBack(msg):
    global resultado_soma
    resultado_soma = msg

def timerCallBack(event):
    msg = String()
    msg.data = '34784'
    pub_matricula.publish(msg)
    
    print('Soma da matricula = '+resultado_soma.data)
    
pub_matricula = rospy.Publisher('/no_matricula/matricula', String, queue_size=1)
sub_matricula = rospy.Subscriber('/no_soma/soma', String, sub_matriculaCallBack)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin() 