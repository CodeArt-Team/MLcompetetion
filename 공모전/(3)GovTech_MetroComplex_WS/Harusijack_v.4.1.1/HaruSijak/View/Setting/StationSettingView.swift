//
//  StationSettingView.swift
//  HaruSijak
//
//  Created by 신나라 on 9/10/24.
/*
    Description : HaruSijack App 개발 setting page
    Date : 2024.09.10
    Author : snr
    Detail :
    Updates :
        * 2024.09.10 by snr : 시간, 역 설정 화면 분리
 */

import SwiftUI

struct StationSettingView: View {
    
    let timeList = [Int](5..<25)            // 5~24까지 리스트
    let line23 = SubwayList().totalStation
    
    let dbModel = TimeSettingDB()           // 시간 설정 vm instance 생성
    @State var infoList: [Time] = []        // 조회된 시간정보 담을 리스트
    @Environment(\.dismiss) var dismiss         // 화면 이동을 위한 변수
    @State var alertType: SettingAlertType?        // 추가, 수정 alert
    @State var titleName : String
    
    @State var selectedTime = 0             // picker뷰 선택 value
    @State var selectedStation = 0          // station 선택 value
    @State var selectedLine = 0             // line 선택 value
    
    @State var line: [Int] = [1, 2, 3, 4, 5, 6, 7, 8]
    
    @Binding var stationValue: String
    @Binding var lineValue: Int
    @Binding var timeValue: Int
    
    @State var buttonTitle = TimeSettingDB().queryDB().isEmpty ? "입력하기" : "수정하기"
    
    
    var filteredStatioins: [(String, Int)] {
        line23.map { ($0.name, $0.intValue1) }
            .filter { $0.1 == selectedLine + 1 }
            .sorted { $0.0 < $1.0 }
    }
    
    
    var body: some View {
            VStack(content: {
                
                //title
                Text(titleName)
                    .font(.custom("Tenada", size: 25).bold())
                    .padding(.top, 20)
                
                
                // ---------------- line picker -------------------
                HStack {
                    Text("호선 선택 : ")
                        .font(.custom("Tenada", size: 20))
                    
                    Picker("", selection: $selectedLine, content: {
                        ForEach(0..<line.count, id:\.self, content: { index in
                            Text("\(line.map{$0}.sorted()[index])호선").tag(index)
                                .font(.custom("Tenada", size: 30))
                        })
                    })
                    .pickerStyle(.menu)
                }
                .padding(.top, 40)
                
                
                // ---------------- station picker -------------------
                HStack {
                    Text("역 선택 : ")
                        .font(.custom("Tenada", size: 20))
                    
                    Picker("", selection: $selectedStation, content: {
                        ForEach(filteredStatioins.indices, id: \.self) { index in
                            Text(self.filteredStatioins[index].0)
                                .frame(minWidth: 100 ,maxWidth: 200, alignment: .center)
                                .tag(index)
                                .font(.custom("Tenada", size: 25))
                        }
                        .pickerStyle(MenuPickerStyle())
                    })
                    .pickerStyle(.menu)
                }
                .frame(maxWidth: .infinity, alignment: .center)
                .padding(.top, 10)
                
                
                // ---------------- 변경 button -------------------
                Button(buttonTitle, action: {
                    infoList = dbModel.queryDB()
                    
                    print("infoList.count : ",infoList.count)
                    
                    // 시간 설정 정보가 없을 때 => insert
                    if infoList.isEmpty {
                        print("infoList is empty, setting isAdd to true")
                        alertType = .add
                        
                    } else {
                        // update 처리
                        print("infoList is not empty, setting isUpdate to true")
                        alertType = .update
                    }
                }) // Button
                
                .font(.custom("Tenada", size: 20))
                .buttonStyle(.bordered)
                .buttonBorderShape(.capsule)
                .background(Color("toolbarColor"))
                .cornerRadius(30)
                .controlSize(.large)
                .foregroundColor(.black)
                .frame(width: 200, height: 50) // 버튼의 크기 조정
                .padding(.top, 40)
                
//                .tint(.black)
                .alert(item: $alertType) { alertType in
                    switch alertType {
                    case .add:
                        return Alert(
                            title: Text("알림"),
                            message: Text("\(filteredStatioins[selectedStation].0)역으로 \n 설정하시겠습니까?"),
                            primaryButton: .destructive(Text("확인"), action: {
                                dbModel.insertDB(time: timeList[selectedTime], station: filteredStatioins[selectedStation].0, line: line[selectedLine])
                                
                                stationValue = filteredStatioins[selectedStation].0
                                lineValue = line[selectedLine]
                                timeValue = timeList[selectedTime]
                                
                                dismiss()
                            }),
                            secondaryButton: .cancel(Text("취소"))
                        )
                    case .update:
                        return Alert(
                            title: Text("알림"),
                            message: Text("\(filteredStatioins[selectedStation].0)역으로 \n 설정하시겠습니까?"),
                            primaryButton: .destructive(Text("확인"), action: {
                                dbModel.updateDB(time: timeList[selectedTime], station: filteredStatioins[selectedStation].0, line: line[selectedLine], id: infoList[0].id)
                               
                                stationValue = filteredStatioins[selectedStation].0
                                lineValue = line[selectedLine]
                                timeValue = timeList[selectedTime]
                                
                                dismiss()
                            }),
                            secondaryButton: .cancel(Text("취소"))
                        )
                    }
                }
            })//VStack
            .onAppear{
                // SettingView에서 넘어오는 Line 값이 임의로 설정한 124일 경우, 1호선부터 조회되도록 selectedLine = 0 처리
                if lineValue == 124 {
                    selectedLine = 0 // 1호선부터 출력되도록
                } else {
                    selectedLine = lineValue - 1 // 0 : 1호선이므로 -1처리해줌
                    selectedStation = filteredStatioins.firstIndex { $0.0 == stationValue } ?? 0
                    selectedTime = timeList.firstIndex { $0 == timeValue } ?? 0
                }
                
                print("onAppear lineValue : ", lineValue)
                print("onAppear selectedLine : ", selectedLine)
                print("--------------------------------------")
                print("onAppear stationValue : ", stationValue)
                print("onAppear selectedStation : ", selectedStation)
            }
    }
}

#Preview {
    StationSettingView(titleName: "테스트제목", stationValue: .constant("Initial Station Value"), lineValue: .constant(1), timeValue: .constant(1))
}

