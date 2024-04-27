var Status_ = {
    ros : null,
    name : "",
    init : function(ros) {
        this.ros = ros;
        this.mode = "";

        $('#mode').text("Awaiting instructions・受信待ち");
        $('#execution_scene').text("Awaiting instructions・受信待ち");
        $('#battery').text("?");

        this.mode_sub = new ROSLIB.Topic({
            ros : this.ros,
            name : '/mode',
            messageType : 'std_msgs/String'
        });
        this.mode_sub.subscribe(message => {
            if(message.data == "AMR") {
                $('#mode').text("AMR");
                $('#execution_scene').text("Awaiting instructions・受信待ち");
                this.mode = "AMR";
            }
            else if(message.data == "AGV") {
                $('#mode').text("AGV");
                this.mode = "AGV";
            }
            else {
                $('#mode').text("Awaiting instructions・受信待ち");
                $('#execution_scene').text("Awaiting instructions・受信待ち");
                this.mode = "";
            }
        });

        this.execution_scene_sub = new ROSLIB.Topic({
            ros : this.ros,
            name : '/execution_scene',
            messageType : 'lexxauto_msgs/execution_scene'
        });
        this.execution_scene_sub.subscribe(message => {
            if(this.mode == "AGV") { $('#execution_scene').text(message.agv_scenario_mode); }
        });

        this.battery_sub = new ROSLIB.Topic({
            ros : this.ros,
            name : '/sensor_set/battery',
            messageType : 'lexxauto_msgs/Battery'
        });
        this.battery_sub.subscribe(message => {
            $('#battery').text((message.state.percentage * 100.0).toFixed(1));
        });
    }
}
