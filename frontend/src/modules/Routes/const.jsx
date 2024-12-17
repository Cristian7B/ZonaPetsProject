import { AcercaDe } from "../infoPages/pages/acercade/components/AcercaDe";
import { Afiliate } from "../infoPages/pages/afiliate/components/Afiliate";
import { Contacto } from "../infoPages/pages/contacto/contacto/components/Contacto";
import { Faq } from "../infoPages/pages/faq/components/Faq";
import { Respuesta } from "../infoPages/pages/faq/components/Respuesta";
import { Politicas } from "../infoPages/pages/politicasPrivacidad/components/Politicas";
import { PremiumLanding } from "../infoPages/pages/premium/PremiumLanding";
import { Tyc } from "../infoPages/pages/terminosCondiciones/components/Tyc";
import { ZonaPets } from "../mainPage/components/ZonaPets";
import { Registrar } from "../principalPages/generalRegister/components/RegistrarLanding/Registrar";

export const ROUTES = [
    { path: "/", element: <ZonaPets /> },
    { path: "/acercade", element: <AcercaDe /> },
    { path: "/contacto", element: <Contacto /> },
    { path: "/faq", element: <Faq /> },
    { path: "/faq/:category/:question", element: <Respuesta /> },
    { path: "/terminos", element: <Tyc /> },
    { path: "/politicas", element: <Politicas /> },
    { path: "/afiliate", element: <Afiliate /> },
    { path: "/premium", element: <PremiumLanding /> },
    { path: "/registrar", element: <Registrar/>}
];