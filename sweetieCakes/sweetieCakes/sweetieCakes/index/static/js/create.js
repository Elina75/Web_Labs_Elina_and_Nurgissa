/* Button hover effect */
	$('.btn_animated').on('mouseenter', '.circle', function(e){
		if ($(this).find(".ink").length === 0) {
			$(this).prepend("<span class='ink'></span>");
		}
		var ink = $(this).find(".ink");
		ink.removeClass("animate");
		if (!ink.height() && !ink.width()) {
			var d = Math.max($(this).outerWidth(), $(this).outerHeight());
			ink.css({
				height: d,
				width: d
			});
		}
		var x = e.pageX - $(this).offset().left - ink.width() / 2;
		var y = e.pageY - $(this).offset().top - ink.height() / 2;
		ink.css({
			top: y + 'px',
			left: x + 'px'
		}).addClass("animate");
	});