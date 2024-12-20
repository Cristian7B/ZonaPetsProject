import { ButtonContacto } from "./ButtonContacto";
import { Header } from "./Header";
import { Preguntas } from "./Preguntas";
import { Footer } from "../../../../generalPages/components/Footer"
import "../Faq.css"
import { PrincipalNav } from "../../../../generalPages/components/PrincipalNav";

export function Faq() {
    return (
        <>
            <PrincipalNav/>
            <div className="container-all">
                <Header/>
                <Preguntas/>
                <ButtonContacto/>
                <Footer/>
            </div>
        </>
    )
}