import media
import fresh_tomatoes

AravindaSametha = media.Movie("Aravinda Sametha", "Try to change factionisiom",
                  "http://businessoftollywood.com/wp-content/uploads/2018/10/Aravinda-Sametha-Movie-Review.jpg",
                  "https://www.youtube.com/watch?v=dNMe5oRfsCE")
#<iframe width="677" height="381" src="https://www.youtube.com/embed/dNMe5oRfsCE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
Battalion609=media.Movie("Battalion609","War Between Indian Army And Pakisthan Army.",
								"http://orissadiary.com/wp-content/uploads/2018/12/Battalion-609.jpeg","https://www.youtube.com/watch?v=fBIRBAn6OlY")
amvas=media.Movie("Amvas","Horror/Thriller","http://www.discount4sales.com/wp-content/uploads/2018/08/Amavas.jpg","https://www.youtube.com/watch?v=ZnWdBn55EVw")

NTRbiopic=media.Movie("NTR BIOPIC","Life history of sri Nandamuri Tharakaramarao garu","https://i.ndtvimg.com/i/2018-01/ntr-twitter_650x400_51516280130.jpg","https://www.youtube.com/watch?v=yAdcYxGnyZQ")

Kalank=media.Movie("Kalank","Romantic and Comedy Movie","https://i.ytimg.com/vi/aqPKX2te0s4/maxresdefault.jpg","https://www.youtube.com/watch?v=huZx66QlWVg")

Junglee=media.Movie("Junglee","Action Movie","https://images-na.ssl-images-amazon.com/images/I/51LtjQTT6qL.jpg","https://www.youtube.com/watch?v=9mi-6-0KMzI")

movies = [AravindaSametha,Battalion609,amvas,NTRbiopic,Kalank,Junglee]
fresh_tomatoes.open_movies_page(movies)

