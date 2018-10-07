$thumbnail.on('click', function(e){
 e.preventDefault();
 src ="https://www.youtube.com/embed/8rcBlYCKKW8&autoplay=1"; // src: the original URL for embedding
 $videoContainer.empty().append( $iframe.clone().attr({'src': src}) ); // $iframe: the original iframe for embedding
 }
);
