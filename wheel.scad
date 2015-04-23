outer_diameter = 65;
shaft_round_diameter = 5.25; // .25 over measured
shaft_flat_diameter = 3.25; // .25 over measured
shaft_length = 8;
tire_width = 12.5;

difference(){
	union(){
		// outside of wheel
		cylinder(r=outer_diameter / 2, h= tire_width + 2, $fn=100);

		// rim
		cylinder(r=(outer_diameter / 2) + .5, h=2, $fn=100);
		translate([0,0,tire_width + 2]){
			cylinder(r=(outer_diameter / 2) + .5, h=2, $fn=100);
		}
	}

	// shaft hole
	translate([-shaft_flat_diameter / 2,-shaft_round_diameter / 2,-1]){
		//cylinder(r=shaft_round_diameter / 2, h = tire_width + 6);
		cube([shaft_flat_diameter,shaft_round_diameter,tire_width + 6]);
	}

	// webbing
	for(i=[0:4]){
		rotate(i*360/4,[0,0,1]){
			translate([0,outer_diameter / 4,-1]){
				cylinder(r=10,h=tire_width + 6, $fn=100);
			}
		}
	}
	translate([0,0,tire_width * 2.7]){
		sphere(r=outer_diameter / 2, $fn=100);
	}
}

difference(){
	// hub
	cylinder(r=shaft_round_diameter,h=shaft_length, $fn=100);

	// shaft hole
	translate([-shaft_flat_diameter / 2,-shaft_round_diameter / 2,-1]){
		//cylinder(r=shaft_round_diameter / 2, h = tire_width + 6);
		cube([shaft_flat_diameter,shaft_round_diameter,tire_width + 6]);
	}
}