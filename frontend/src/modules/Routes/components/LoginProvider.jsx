import { Route } from "react-router-dom";
import { InicialLandingLogin } from "../../principalPages/loginUser/components/InicialLanding";
import { AccountLogin } from "../../principalPages/loginUser/components/AccountLogin";
import { AccountRegister } from "../../principalPages/loginUser/components/AccountRegister";

export function LoginProvider() {
    return (
        <>
            <Route path="/iniciarsesion" element={<InicialLandingLogin />} />
            <Route path="/iniciarsesion/login" element={<AccountLogin />} />
            <Route path="/iniciarsesion/registrar" element={<AccountRegister />} />
        </>
    )
}