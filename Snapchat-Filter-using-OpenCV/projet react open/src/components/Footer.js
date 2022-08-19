import { useState } from 'react'
import '../styles/Footer.css'

function Footer() {
	const [inputValue, setInputValue] = useState('')

	function handleInput(e) {
		setInputValue(e.target.value)
	}

	function handleBlur() {
		if (!inputValue.includes('@')) {
			alert("Attention, il n'y a pas d'@, ceci n'est pas une adresse valide 😥")
		}
	}

	return (
		<footer className='lmj-footer'>
		    <div className="about">
		    	<h4>A propos</h4>
		    	<p>
		    		Je suis Nazirah, une étudiante à l'ESTI parcours développment web.
		    		Je suis passionée de tout ce qui concerne la nouvelle technologie,
		    		membre de la communauté ITEAM$.
		    	</p>
		    </div>
			<div className="contact">
				<div className='lmj-footer-elem'>
					<strong>Pour les passionné·e·s de plantes</strong> 🌿🌱🌵
				</div>
				<div className='lmj-footer-elem'>Laissez-nous votre message :</div>
				<form>
					<div className="form-element">
						<label>Nom</label>
						<input className="form-input" placeholder="John Doe" />
						<label>E-mail</label>
						<input
							placeholder='Entrez votre mail'
							onChange={handleInput}
							value={inputValue}
							onBlur={handleBlur}
							className="form-input mr-0"
						/>
					</div>
					<div className="form-element">
						<label>Message</label>
						<textarea className="form-input mr-0"></textarea>
					</div>
					<div className="form-element justify-end">
						<button>Envoyer</button>
					</div>
				</form>
			</div>
		</footer>
	)
}

export default Footer
