import rospy

from std_msgs.msg import String

rospy.init_node('no_soma')


numero_matricula = String()

def sub_somaCallBack(msg):
    global numero_matricula
    numero_matricula = msg

    
def timerCallBack(event):
    soma = 0
    for k in range(len(numero_matricula.data)):
        soma = soma+int(numero_matricula.data[k]);
 
    msg = String()
    msg.data = str(soma)
    pub_soma.publish(msg)
 

sub_soma = rospy.Subscriber('/no_matricula/matricula', String, sub_somaCallBack)
pub_soma = rospy.Publisher('/no_soma/soma', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin() 