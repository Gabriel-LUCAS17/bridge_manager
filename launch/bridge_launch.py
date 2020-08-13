from simple_launch import SimpleLauncher

def generate_launch_description():
    sl = SimpleLauncher()
    
    sl.robot_state_publisher('baxter_description', 'baxter.urdf.xacro')
    sl.node('bridge_manager', 'static_bridge_joint_states')
    sl.node('bridge_manager', 'static_bridge_left_joint_command')
    sl.node('bridge_manager', 'static_bridge_right_joint_command')
    
    rviz_config = sl.find('bridge_manager', 'baxter_sim_config.rviz', 'launch/')
    sl.node('rviz2', 'rviz2', arguments = ['-d', rviz_config])
    
    return sl.launch_description()
