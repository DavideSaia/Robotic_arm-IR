#!/usr/bin/python3
import rospy
import tf2_ros
import tf_conversions
import geometry_msgs.msg
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped



def get_transform():
    rospy.init_node('tf2_listener', anonymous=True)

    #Inizializzazione del broadcaster
    broadcaster = tf2_ros.TransformBroadcaster()
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:

            transform = tfBuffer.lookup_transform('world','ef',rospy.Time())

            print("Traslazione rispetto a X: {}".format(transform.transform.translation.x))
            print("Traslazione rispetto a Y: {}".format(transform.transform.translation.y))
            print("Rotazione (Quaternione) rispetto a X: {}".format(transform.transform.rotation.x))

            #Nuova Trasformata per effettuare il broadcast
            transform_stamped = TransformStamped()

            # Header:
            # - stamp
            # - frame_id (Stringa)
            # - child_frame_id (Stringa)

            #stamp
            transform_stamped.header.stamp = rospy.Time.now()
            #frame_id
            transform_stamped.header.frame_id = "world"
            #child_frame_id
            transform_stamped.child_frame_id = "ef_world"

            #translation
            transform_stamped.transform.translation.x = transform.transform.translation.x
            transform_stamped.transform.translation.y = transform.transform.translation.y
            transform_stamped.transform.translation.z = transform.transform.translation.z


            #rotation (Quaternion x,y,z,w)
            transform_stamped.transform.rotation.x = transform.transform.rotation.x
            #rotation y
            transform_stamped.transform.rotation.y = transform.transform.rotation.y
            #rotation z
            transform_stamped.transform.rotation.z = transform.transform.rotation.z
            #rotation w
            transform_stamped.transform.rotation.w = transform.transform.rotation.w

            #broadcast della nuova trasfromata
            broadcaster.sendTransform(transform_stamped)

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            print("Error obtaining transform: ", e)
        rate.sleep()


if __name__ == '__main__':
    get_transform()
    rospy.spin()
