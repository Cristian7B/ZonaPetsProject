import { ItemMomento } from "./ItemMomento";
import { Portada } from "./Portada";
import { QueOfrecemos } from "./QueOfrecemos";
import { ZonaPetsInfo } from "./ZonaPetsInfo"
import { Mision } from "./Mision"
import { Objetivos } from "./Objetivos"
import { SwiperComp } from "./Swiper";
import { Footer } from "../../../../generalPages/components/Footer";
import "../AcercaDe.css"
import { PrincipalNav } from "../../../../generalPages/components/PrincipalNav";
export function AcercaDe() {
    return (
        <>
            <PrincipalNav/>
            <Portada/>
            <div className="container-all">
                <ItemMomento/>
                <QueOfrecemos/>
                <ZonaPetsInfo/>
                <Mision/>
                <Objetivos/>
                <SwiperComp/>
            </div>
            <Footer/>
        </>
    )
}