
// MARK: -- Description
/*
 Description : HaruSijack App splash 화면
 Date : 2024.6.14
 Author : j.park
 Dtail :
 Updates :
 * 2024.06.14 by j.park : 1.splash화면 생성
                          2. Lotti 적용
 
 */

//

import SwiftUI
import Lottie

struct SplashView: View {
    @State private var isActive = false
    
    var body: some View {
        VStack {
            
            Spacer()
            ZStack {
                LottieView(jsonName: "train2")
                    .frame(width: 400, height: 400)
                Spacer()
                
                Text("언제언잼?")
                    .font(.custom("Tenada", size: 30))
                    .foregroundColor(.black)
                    .offset(y: 120)
        
            }
            
            Spacer()
            Spacer()
            
        }
        .onAppear {
            DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                withAnimation {
                    self.isActive = true
                }
            }
        }
        //메인화면으로 이동
        .fullScreenCover(isPresented: $isActive) {
            PredictView03()
        }
    }
}

#Preview {
    SplashView()
}
